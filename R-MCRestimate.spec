%global packname  MCRestimate
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.10.0
Release:          1%{?dist}
Summary:          Misclassification error estimation with cross-validation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-golubEsets 
Requires:         R-e1071 R-pamr R-randomForest R-RColorBrewer R-Biobase R-graphics R-grDevices R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-golubEsets
BuildRequires:    R-e1071 R-pamr R-randomForest R-RColorBrewer R-Biobase R-graphics R-grDevices R-stats R-utils 


%description
This package includes a function for combining preprocessing and
classification methods to calculate misclassification errors

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/MCRestimate/html
%doc %{rlibdir}/MCRestimate/DESCRIPTION
%doc %{rlibdir}/MCRestimate/doc
%{rlibdir}/MCRestimate/INDEX
%{rlibdir}/MCRestimate/scripts
%{rlibdir}/MCRestimate/help
%{rlibdir}/MCRestimate/R
%{rlibdir}/MCRestimate/NAMESPACE
%{rlibdir}/MCRestimate/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.10.0-1
- initial package for Fedora
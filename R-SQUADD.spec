%global packname  SQUADD
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Add-on of the SQUAD Software

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-graphics R-grDevices R-methods R-RColorBrewer R-stats R-utils 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-graphics R-grDevices R-methods R-RColorBrewer R-stats R-utils 


%description
This package SQUADD is a SQUAD add-on. It permits to generate SQUAD
simulation matrix, prediction Heat-Map and Correlation Circle from PCA

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
%doc %{rlibdir}/SQUADD/DESCRIPTION
%doc %{rlibdir}/SQUADD/html
%doc %{rlibdir}/SQUADD/doc
%{rlibdir}/SQUADD/NAMESPACE
%{rlibdir}/SQUADD/Meta
%{rlibdir}/SQUADD/help
%{rlibdir}/SQUADD/INDEX
%{rlibdir}/SQUADD/R
%{rlibdir}/SQUADD/extdata

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora
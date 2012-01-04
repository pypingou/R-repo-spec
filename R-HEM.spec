%global packname  HEM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.26.0
Release:          1%{?dist}
Summary:          Heterogeneous error model for identification of differentially expressed genes under multiple conditions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-Biobase R-grDevices R-stats R-utils 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Biobase R-grDevices R-stats R-utils 


%description
This package fits heterogeneous error models for analysis of microarray

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
%doc %{rlibdir}/HEM/DESCRIPTION
%doc %{rlibdir}/HEM/doc
%doc %{rlibdir}/HEM/html
%{rlibdir}/HEM/R
%{rlibdir}/HEM/help
%{rlibdir}/HEM/INDEX
%{rlibdir}/HEM/libs
%{rlibdir}/HEM/NAMESPACE
%{rlibdir}/HEM/Meta
%{rlibdir}/HEM/data

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.26.0-1
- initial package for Fedora
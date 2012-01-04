%global packname  affy
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.32.0
Release:          1%{?dist}
Summary:          Methods for Affymetrix Oligonucleotide Arrays

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase 
Requires:         R-affyio R-Biobase R-BiocInstaller R-graphics R-grDevices R-methods R-preprocessCore R-stats R-utils R-zlibbioc 

BuildRequires:    R-devel tex(latex) R-Biobase
BuildRequires:    R-affyio R-Biobase R-BiocInstaller R-graphics R-grDevices R-methods R-preprocessCore R-stats R-utils R-zlibbioc 


%description
The package contains functions for exploratory oligonucleotide array
analysis. The dependence on tkWidgets only concerns few convenience
functions. 'affy' is fully functional without it.

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
%doc %{rlibdir}/affy/html
%doc %{rlibdir}/affy/doc
%doc %{rlibdir}/affy/NEWS
%doc %{rlibdir}/affy/CITATION
%doc %{rlibdir}/affy/DESCRIPTION
%{rlibdir}/affy/help
%{rlibdir}/affy/INDEX
%{rlibdir}/affy/demo
%{rlibdir}/affy/data
%{rlibdir}/affy/Meta
RPM build errors:
%{rlibdir}/affy/R
%{rlibdir}/affy/tests
%{rlibdir}/affy/NAMESPACE
%{rlibdir}/affy/libs

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.32.0-1
- initial package for Fedora
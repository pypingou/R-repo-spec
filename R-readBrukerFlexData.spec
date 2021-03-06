%global packname  readBrukerFlexData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.4
Release:          1%{dist}
Summary:          Reads mass spectrometry data in Bruker *flex format

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Reads files generated by MALDI-TOF MS of Bruker Daltonics' *flex series.
Successfully tested for Bruker Daltonics' Autoflex MS.

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
%doc %{rlibdir}/readBrukerFlexData/html
%doc %{rlibdir}/readBrukerFlexData/DESCRIPTION
%doc %{rlibdir}/readBrukerFlexData/NEWS
%{rlibdir}/readBrukerFlexData/Examples
%{rlibdir}/readBrukerFlexData/Meta
%{rlibdir}/readBrukerFlexData/NAMESPACE
%{rlibdir}/readBrukerFlexData/R
%{rlibdir}/readBrukerFlexData/LICENSE
%{rlibdir}/readBrukerFlexData/help
%{rlibdir}/readBrukerFlexData/data
%{rlibdir}/readBrukerFlexData/INDEX

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.4-1
- Update to version 1.2.4

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora
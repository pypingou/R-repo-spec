%global packname  spgwr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.13
Release:          1%{?dist}
Summary:          Geographically weighted regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-13.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-sp R-maptools 

BuildRequires:    R-devel tex(latex) R-sp R-maptools 

%description
Functions for computing geographically weighted regressions based on work
by Chris Brunsdon, Martin Charlton and Stewart Fortheringham,

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
%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.13-1
- initial package for Fedora
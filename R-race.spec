%global packname  race
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.58
Release:          1%{?dist}
Summary:          Racing methods for the selection of the best

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Implementation of some racing methods for the empirical selection of the
best. If the R package `rpvm' is installed (and if PVM is available,
properly configured, and initialized), the evaluation of the candidates
are performed in parallel on different hosts.

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
%doc %{rlibdir}/race/DESCRIPTION
%doc %{rlibdir}/race/COPYING
%doc %{rlibdir}/race/html
%{rlibdir}/race/help
%{rlibdir}/race/slave
%{rlibdir}/race/INDEX
%{rlibdir}/race/Meta
%{rlibdir}/race/examples
%{rlibdir}/race/R
%{rlibdir}/race/COPYRIGHTS
%{rlibdir}/race/ACKNOWLEDGMENTS

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.58-1
- initial package for Fedora
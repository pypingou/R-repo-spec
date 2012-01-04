%global packname  skills
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Skills in Knowledge Space Theory

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-sets R-relations R-grid R-DAKS R-plyr 


BuildRequires:    R-devel tex(latex) R-sets R-relations R-grid R-DAKS R-plyr



%description
Connection between skills and knowledge states in knowledge space theory
and test approaches for empirical knowlege structures according to
Duentsch and Gediga and Doignon and Falmagne

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
%doc %{rlibdir}/skills/html
%doc %{rlibdir}/skills/DESCRIPTION
%{rlibdir}/skills/Meta
%{rlibdir}/skills/INDEX
%{rlibdir}/skills/help
%{rlibdir}/skills/NAMESPACE
%{rlibdir}/skills/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora
%global packname  msSurv
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Nonparametric Estimation for Multistate Models

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-class R-graph R-lattice 

BuildRequires:    R-devel tex(latex) R-methods R-class R-graph R-lattice 

%description
Nonparametric estimation for right censored, left truncated time to event
data in multistate models

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
%doc %{rlibdir}/msSurv/DESCRIPTION
%doc %{rlibdir}/msSurv/html
%{rlibdir}/msSurv/help
%{rlibdir}/msSurv/Meta
%{rlibdir}/msSurv/data
%{rlibdir}/msSurv/R
%{rlibdir}/msSurv/NAMESPACE
%{rlibdir}/msSurv/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora
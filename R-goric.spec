%global packname  goric
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          Generalized Order-Restricted Information Criterion

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm R-quadprog 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-quadprog 

%description
Generalized Order-Restricted Information Criterion (GORIC) value for a set
of hypotheses in multivariate regression models

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
%doc %{rlibdir}/goric/DESCRIPTION
%doc %{rlibdir}/goric/html
%{rlibdir}/goric/Meta
%{rlibdir}/goric/help
%{rlibdir}/goric/INDEX
%{rlibdir}/goric/data
%{rlibdir}/goric/R
%{rlibdir}/goric/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.2-1
- initial package for Fedora
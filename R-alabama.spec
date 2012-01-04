%global packname  alabama
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2011.9.1
Release:          1%{?dist}
Summary:          Constrained nonlinear optimization

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.9-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-numDeriv 

BuildRequires:    R-devel tex(latex) R-numDeriv 

%description
Augmented Lagrangian Adaptive Barrier Minimization Algorithm for
optimizing smooth nonlinear objective functions with constraints. Linear
or nonlinear equality and inequality constraints are allowed.

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
%doc %{rlibdir}/alabama/NEWS
%doc %{rlibdir}/alabama/html
%doc %{rlibdir}/alabama/DESCRIPTION
%{rlibdir}/alabama/Meta
%{rlibdir}/alabama/demo
%{rlibdir}/alabama/INDEX
%{rlibdir}/alabama/R
%{rlibdir}/alabama/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.9.1-1
- initial package for Fedora
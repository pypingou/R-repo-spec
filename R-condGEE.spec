%global packname  condGEE
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Parameter estimation in conditional GEE for recurrent event gap times

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-numDeriv R-rootSolve 

BuildRequires:    R-devel tex(latex) R-numDeriv R-rootSolve 

%description
Solves for the mean parameters, the variance parameter, and their
asymptotic variance in a conditional GEE for recurrent event gap times, as
described by Clement and Strawderman (2009) in the journal Biostatistics.
Makes a parametric assumption for the length of the censored gap time.

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
%doc %{rlibdir}/condGEE/html
%doc %{rlibdir}/condGEE/DESCRIPTION
%{rlibdir}/condGEE/Meta
%{rlibdir}/condGEE/R
%{rlibdir}/condGEE/data
%{rlibdir}/condGEE/help
%{rlibdir}/condGEE/demo
%{rlibdir}/condGEE/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora
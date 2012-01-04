%global packname  galts
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Genetic algorithms and C-steps based LTS (Least Trimmed Squares) estimation

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-genalg R-DEoptim 

BuildRequires:    R-devel tex(latex) R-genalg R-DEoptim 

%description
This package includes the ga.lts function that estimates LTS (Least
Trimmed Squares) parameters using genetic algorithms and C-steps. ga.lts()
constructs a genetic algorithm to form a basic subset and iterates C-steps
as defined in Rousseeuw and van-Driessen (2006) to calculate the cost
value of the LTS criterion. OLS(Ordinary Least Squares) regression is
known to be sensitive to outliers. A single outlying observation can
change the values of estimated parameters. LTS is a resistant estimator
even the number of outliers is up to half of the data. This package is for
estimating the LTS parameters with lower bias and variance in a reasonable

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
%doc %{rlibdir}/galts/html
%doc %{rlibdir}/galts/DESCRIPTION
%{rlibdir}/galts/INDEX
%{rlibdir}/galts/Meta
%{rlibdir}/galts/R
%{rlibdir}/galts/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora
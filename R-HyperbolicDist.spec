%global packname  HyperbolicDist
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.2
Release:          1%{?dist}
Summary:          The hyperbolic distribution

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provides functions for the hyperbolic and related
distributions. Density, distribution and quantile functions and random
number generation are provided for the hyperbolic distribution, the
generalized hyperbolic distribution, the generalized inverse Gaussian
distribution and the skew-Laplace distribution. Additional functionality
is provided for the hyperbolic distribution, including fitting of the
hyperbolic to data.

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
%doc %{rlibdir}/HyperbolicDist/NEWS
%doc %{rlibdir}/HyperbolicDist/html
%doc %{rlibdir}/HyperbolicDist/DESCRIPTION
%{rlibdir}/HyperbolicDist/Meta
%{rlibdir}/HyperbolicDist/R
%{rlibdir}/HyperbolicDist/INDEX
%{rlibdir}/HyperbolicDist/data
%{rlibdir}/HyperbolicDist/help
%{rlibdir}/HyperbolicDist/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.2-1
- initial package for Fedora
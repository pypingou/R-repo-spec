%global packname  energy
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          E-statistics (energy statistics)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-boot R-MASS 

BuildRequires:    R-devel tex(latex) R-boot R-MASS 

%description
E-statistics (energy) tests and statistics for comparing distributions:
multivariate normality, multivariate distance components and k-sample test
for equal distributions, hierarchical clustering by e-distances,
multivariate independence tests, distance correlation, goodness-of-fit
tests. Energy-statistics concept based on a generalization of Newton's
potential energy is due to Gabor J. Szekely.

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
%doc %{rlibdir}/energy/html
%doc %{rlibdir}/energy/DESCRIPTION
%doc %{rlibdir}/energy/NEWS
%{rlibdir}/energy/R
%{rlibdir}/energy/help
%{rlibdir}/energy/INDEX
%{rlibdir}/energy/Meta
%{rlibdir}/energy/NAMESPACE
%{rlibdir}/energy/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora
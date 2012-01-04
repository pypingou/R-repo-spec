%global packname  nFactors
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.3.2
Release:          1%{?dist}
Summary:          Parallel Analysis and Non Graphical Solutions to the Cattell Scree Test

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-psych R-boot R-lattice 

BuildRequires:    R-devel tex(latex) R-MASS R-psych R-boot R-lattice 

%description
Indices, heuristics and strategies to help determine the number of
factors/components to retain: 1. Acceleration factor (af with or without
Parallel Analysis); 2. Optimal Coordinates (noc with or without Parallel
Analysis); 3. Parallel analysis (components, factors and bootstrap); 4.
lambda > mean(lambda) (Kaiser, CFA and related); 5. Cattell-Nelson-Gorsuch
(CNG); 6. Zoski and Jurs multiple regression (b, t and p); 7. Zoski and
Jurs standard error of the regression coeffcient (sescree); 8. Nelson R2;
9. Bartlett khi-2; 10. Anderson khi-2; 11. Lawley khi-2 and 12.
Bentler-Yuan khi-2.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.2-1
- initial package for Fedora
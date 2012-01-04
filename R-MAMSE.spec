%global packname  MAMSE
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Calculation of Minimum Averaged Mean Squared Error (MAMSE) weights.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package calculates the nonparametric adaptive MAMSE weights for
univariate, right-censored or multivariate data. The MAMSE weights can be
used in a weighted likelihood or to define a mixture of empirical
distribution functions.

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
%doc %{rlibdir}/MAMSE/DESCRIPTION
%doc %{rlibdir}/MAMSE/html
%{rlibdir}/MAMSE/help
%{rlibdir}/MAMSE/R
%{rlibdir}/MAMSE/INDEX
%{rlibdir}/MAMSE/NAMESPACE
%{rlibdir}/MAMSE/libs
%{rlibdir}/MAMSE/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora
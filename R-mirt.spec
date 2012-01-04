%global packname  mirt
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.19
Release:          1%{?dist}
Summary:          Multidimensional Item Response Theory

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-19.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-lattice R-psych R-GPArotation R-mvtnorm R-Matrix 

BuildRequires:    R-devel tex(latex) R-methods R-lattice R-psych R-GPArotation R-mvtnorm R-Matrix 

%description
Analysis of dichotomous and polychotomous response data using latent trait
models under the Item Response Theory paradigm. Includes the multivariate
two- and three-parameter logistic models, confirmatory bifactor analysis,
polytomous confirmatory and exploratory item response models, and
partially-compensatory item response modeling in conjunction with other
IRT models.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.19-1
- initial package for Fedora
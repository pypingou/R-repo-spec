%global packname  FitAR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.92
Release:          1%{?dist}
Summary:          Subset AR Model Fitting

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-leaps R-ltsa R-bestglm 

BuildRequires:    R-devel tex(latex) R-lattice R-leaps R-ltsa R-bestglm 

%description
Comprehensive model building function for identification, estimation and
diagnostic checking for AR and subset AR models. Two types of subset AR
models are supported.  One family of subset AR models, denoted by ARp, is
formed by taking subet of the original AR coefficients and in the other,
denoted by ARz, subsets of the partial autocorrelations are used. The main
advantage of the ARz model is its applicability to very large order

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.92-1
- initial package for Fedora
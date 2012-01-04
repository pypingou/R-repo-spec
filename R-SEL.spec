%global packname  SEL
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Semiparametric elicitation

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-splines R-quadprog R-lattice 

BuildRequires:    R-devel tex(latex) R-splines R-quadprog R-lattice 

%description
This package implements a novel method for fitting a bounded probability
distribution to quantiles (for example stated by an expert), see Bornkamp
and Ickstadt (2009) for details.  For this purpose B-splines are used, and
the density is obtained by penalized least squares based on a Brier
entropy penalty.  The package provides methods for fitting the
distribution as well as methods for evaluating the underlying density and
cdf. In addition methods for plotting the distribution, drawing random
numbers and calculating quantiles of the obtained distribution are

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
%doc %{rlibdir}/SEL/html
%doc %{rlibdir}/SEL/DESCRIPTION
%{rlibdir}/SEL/Meta
%{rlibdir}/SEL/libs
%{rlibdir}/SEL/help
%{rlibdir}/SEL/R
%{rlibdir}/SEL/NAMESPACE
%{rlibdir}/SEL/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora
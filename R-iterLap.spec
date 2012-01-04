%global packname  iterLap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Approximate probability densities by iterated Laplace Approximations

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-quadprog R-randtoolbox R-parallel 


BuildRequires:    R-devel tex(latex) R-quadprog R-randtoolbox R-parallel



%description
The iterLap (iterated Laplace approximation) algorithm approximates a
general (possibly non-normalized) probability density on R^p, by repeated
Laplace approximations to the difference between current approximation and
true density (on log scale). The final approximation is a mixture of
multivariate normal distributions and might be used for example as a
proposal distribution for importance sampling (eg in Bayesian
applications). The algorithm can be seen as a computational generalization
of the Laplace approximation suitable for skew or multimodal densities.

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
%doc %{rlibdir}/iterLap/html
%doc %{rlibdir}/iterLap/DESCRIPTION
%doc %{rlibdir}/iterLap/CITATION
%{rlibdir}/iterLap/help
%{rlibdir}/iterLap/NAMESPACE
%{rlibdir}/iterLap/INDEX
%{rlibdir}/iterLap/Meta
%{rlibdir}/iterLap/R
%{rlibdir}/iterLap/libs

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora
%global packname  abn
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Additive Bayesian Networks

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A graphical modelling formulation is used to construct Bayesian regression
models for analyses of multivariate data. The models comprise of directed
acyclic graphs where each node in the graph comprises a generalized linear
model, and a greedy search heuristic is used to identify high scoring
models that attempt to identify relationships between all variables in the
data. Currently implemented are models for data comprising of categorical
(Binomial with logit link) and/or continuous (Gaussian with identity link)
variables. Laplace approximations are used to estimate marginal
likelihoods and compute marginal posterior densities.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.1-1
- initial package for Fedora
%global packname  BPHO
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          Bayesian Prediction with High-order Interactions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This software can be used in two situations. The first is to predict the
next outcome based on the previous states of a discrete sequence. The
second is to classify a discrete response based on a number of discreate
covariates. In both situations, we use Bayesian logistic regression models
that consider the high-order interactions. The models are trained with
slice sampling method, a variant of Markov chain Monte Carlo. The time
arising from using high-order interactions is reduced greatly by our
compression technique that represents a group of original parameters as a
single one in MCMC step.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.0-1
- initial package for Fedora
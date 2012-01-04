%global packname  VBMA4hmm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          The VBMA4hmm (Variational Bayesian Markov Model for hidden markov model) package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package allows one to deal with a 2-states HMM with a fixed Gaussian
distribution as emission for one state and a mixture of Gaussian for the
other state. Furthermore, by computing optimal variational weights, it
calculates an averaged estimator of the posterior probabilities.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora
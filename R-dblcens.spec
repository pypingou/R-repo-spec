%global packname  dblcens
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.6
Release:          1%{?dist}
Summary:          Compute the NPMLE of distribution from doubly censored data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Use EM algorithm to compute the NPMLE of CDF and also the two censoring
distributions. For doubly censored data (as described in Chang and Yang
(1987) Ann. Stat. 1536-47). You can also specify a constraint, it will
return the constrained NPMLE and the -2 log empirical likelihood ratio.
This can be used to test the hypothesis about the constraint and find
confidence intervals for probability or quantile via empirical likelihood
ratio theorem. Influence function of hat F may also be calculated (but may
be slow). It also include a new iterative computation of the
self-consistant estimator of CDF from doubly censored data.

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
%doc %{rlibdir}/dblcens/html
%doc %{rlibdir}/dblcens/DESCRIPTION
%{rlibdir}/dblcens/help
%{rlibdir}/dblcens/NAMESPACE
%{rlibdir}/dblcens/Meta
%{rlibdir}/dblcens/R
%{rlibdir}/dblcens/libs
%{rlibdir}/dblcens/data
%{rlibdir}/dblcens/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.6-1
- initial package for Fedora
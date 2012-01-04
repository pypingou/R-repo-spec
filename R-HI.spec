%global packname  HI
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Simulation from distributions supported by nested hyperplanes

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Simulation from distributions supported by nested hyperplanes, using the
algorithm described in Petris & Tardella, "A geometric approach to
transdimensional Markov chain Monte Carlo", Canadian Journal of
Statistics, v.31, n.4, (2003). Also random direction multivariate Adaptive
Rejection Metropolis Sampling.

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
%doc %{rlibdir}/HI/DESCRIPTION
%doc %{rlibdir}/HI/html
%{rlibdir}/HI/libs
%{rlibdir}/HI/Meta
%{rlibdir}/HI/INDEX
%{rlibdir}/HI/R
%{rlibdir}/HI/NAMESPACE
%{rlibdir}/HI/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora
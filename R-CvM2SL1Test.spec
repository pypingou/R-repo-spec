%global packname  CvM2SL1Test
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          L1-version of Cramer-von Mises Two Sample Tests

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The package contains two functions for L1-version of Cramer-von Mises
Tests: one computes Cramer-von Mises two sample test scores, the other
cmoputes the exact p-value(s) for given Cramer-von Mises two-sample test
score(s) under the assumption that the populations under comparison have
the same probability distribution. The L1-version Cramer-von Mises test,
like its L2 counterpart, is distribution-free, but of less computational
intensity. In certain cases, this version of Cramer-von Mises test is
almost as powerful as its L2 counterpart. Simulation study also shows that
it is more powerful than the Kolmogorov-Smirnov test in certain cases.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora
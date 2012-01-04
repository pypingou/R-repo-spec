%global packname  phitest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Nonparametric goodness-of-fit methods based on phi-divergences

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package perform a generalized goodness-of-fit test based on
phi-divergences.  This test works by considering the maximum 'distance'
between the hypothesized distribution function and the empirical
distribution function, where the measure of 'distance' is based on a
phi-divergence.  This generalized family of tests is indexed by a
real-valued parameter, s, wich can take values in [-1,2].  Special cases
of this family include the Berk-Jones statistic (s=0), the supremum form
of the Anderson-Darling statistic (s=2), and the statistic of Jaescke and
Eicker (s=-1).  See the references for the phi.test() function for
references regarding these special cases.  In addition to performing a
statistical test, this package will also invert the test statistic to form
and plot confidence bands for the true distribution function for sample
sizes up to 10,000.

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
%doc %{rlibdir}/phitest/html
%doc %{rlibdir}/phitest/DESCRIPTION
%{rlibdir}/phitest/NAMESPACE
%{rlibdir}/phitest/libs
%{rlibdir}/phitest/INDEX
%{rlibdir}/phitest/help
%{rlibdir}/phitest/Meta
%{rlibdir}/phitest/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora
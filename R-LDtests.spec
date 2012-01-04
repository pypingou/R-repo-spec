%global packname  LDtests
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Exact tests for Linkage Disequilibrium and Hardy-Weinberg Equilibrium

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Exact tests for Linkage Disequilibrium (LD) and Hardy-Weinberg Equilibrium
(HWE). - 2-sided LD tests based on different measures of LD (Kulinskaya
and Lewin 2008) - 1-sided Fisher's exact test for LD - 2-sided Haldane
test for HWE (Wiggington 2005) - 1-sided test for inbreeding - conditional
p-values proposed in Kulinskaya (2008) to overcome the problems of
asymetric distributions (for both LD and HWE)

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
%doc %{rlibdir}/LDtests/DESCRIPTION
%doc %{rlibdir}/LDtests/html
%{rlibdir}/LDtests/R
%{rlibdir}/LDtests/NAMESPACE
%{rlibdir}/LDtests/help
%{rlibdir}/LDtests/INDEX
%{rlibdir}/LDtests/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora
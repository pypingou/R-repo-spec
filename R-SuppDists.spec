%global packname  SuppDists
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.8
Release:          1%{?dist}
Summary:          Supplementary distributions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Ten distributions supplementing those built into R. Inverse Gauss,
Kruskal-Wallis, Kendall's Tau, Friedman's chi squared, Spearman's rho,
maximum F ratio, the Pearson product moment correlation coefficiant,
Johnson distributions, normal scores and generalized hypergeometric
distributions. In addition two random number generators of George
Marsaglia are included.

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
%doc %{rlibdir}/SuppDists/DESCRIPTION
%doc %{rlibdir}/SuppDists/html
%{rlibdir}/SuppDists/help
%{rlibdir}/SuppDists/NAMESPACE
%{rlibdir}/SuppDists/libs
%{rlibdir}/SuppDists/Meta
%{rlibdir}/SuppDists/R
%{rlibdir}/SuppDists/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.8-1
- initial package for Fedora
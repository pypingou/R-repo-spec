%global packname  BiasedUrn
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.04
Release:          1%{?dist}
Summary:          Biased Urn model distributions

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Statistical models of biased sampling in the form of univariate and
multivariate noncentral hypergeometric distributions, including Wallenius'
noncentral hypergeometric distribution and Fisher's noncentral
hypergeometric distribution (also called extended hypergeometric
distribution). See vignette("UrnTheory") for explanation of these

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.04-1
- initial package for Fedora
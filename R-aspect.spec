%global packname  aspect
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Aspects of Multivariables

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package consists of two main functions. The first function is
corAspect() performs optimal scaling by maximizing an aspect (i.e. target
function such as sum eigenvalues, sum of squared correlations, squared
multiple correlations, etc.) of the corresponding correlation matrix. The
second function is lineals() which performs optimal scaling by
mimimization a non-correlational aspect based on pairwise correlations and
correlation ratios. The resulting correlation matrix and category scores
can be used for further multivariate methods such as SEM. A platform
including related PsychoR packages is provided on R-Forge.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora
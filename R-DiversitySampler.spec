%global packname  DiversitySampler
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Functions for re-sampling a community matrix to compute diversity indices at different sampling levels.

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
There are two functions in this package, which can be used together to
estimate the Shannon's Diversity index at different levels of sample size.
A Monte-Carlo procedure is used to re-sample a given observation at each
level of sampling. The expectation being that the mean of the re-sampling
will approach Shannon's diversity index at that sample level.

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
%doc %{rlibdir}/DiversitySampler/DESCRIPTION
%doc %{rlibdir}/DiversitySampler/html
%{rlibdir}/DiversitySampler/R
%{rlibdir}/DiversitySampler/NAMESPACE
%{rlibdir}/DiversitySampler/help
%{rlibdir}/DiversitySampler/INDEX
%{rlibdir}/DiversitySampler/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora
%global packname  sporm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Semiparametric proportional odds rate model

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
R implementation of the methods described in "A rank-based empirical
likelihood approach to two-sample proportional odds model and its
goodness-of-fit" by Zhong Guan and Cheng Peng, Journal of Nonparametric
Statistics, to appear.

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
%doc %{rlibdir}/sporm/DESCRIPTION
%doc %{rlibdir}/sporm/html
%{rlibdir}/sporm/INDEX
%{rlibdir}/sporm/Meta
%{rlibdir}/sporm/NAMESPACE
%{rlibdir}/sporm/R
%{rlibdir}/sporm/data
%{rlibdir}/sporm/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora
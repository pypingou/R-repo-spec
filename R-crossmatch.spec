%global packname  crossmatch
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          The cross-match test

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nbpMatching 

BuildRequires:    R-devel tex(latex) R-nbpMatching 

%description
This package performs a test for comparing two multivariate distributions
by using the distance between observations.  The input is a distance
matrix and the labels of the two groups to be compared, the output is the
number of cross-matches and a p-value.

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
%doc %{rlibdir}/crossmatch/DESCRIPTION
%doc %{rlibdir}/crossmatch/html
%{rlibdir}/crossmatch/INDEX
%{rlibdir}/crossmatch/Meta
%{rlibdir}/crossmatch/help
%{rlibdir}/crossmatch/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora
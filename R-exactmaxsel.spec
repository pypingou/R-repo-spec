%global packname  exactmaxsel
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Maximally selected statistics for binary response variables - Exact methods

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-combinat 

BuildRequires:    R-devel tex(latex) R-combinat 

%description
This package computes the exact distribution of some maximally selected
statistics in the following setting: the 'response' variable is binary,
the splitting variable may be nominal, ordinal or continuous. Currently,
the package implements the chi-square statistic and the Gini-index.

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
%doc %{rlibdir}/exactmaxsel/html
%doc %{rlibdir}/exactmaxsel/DESCRIPTION
%{rlibdir}/exactmaxsel/R
%{rlibdir}/exactmaxsel/help
%{rlibdir}/exactmaxsel/data
%{rlibdir}/exactmaxsel/Meta
%{rlibdir}/exactmaxsel/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora
%global packname  st
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.6
Release:          1%{?dist}
Summary:          Shrinkage t Statistic and CAT Score

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-sda R-fdrtool 


BuildRequires:    R-devel tex(latex) R-sda R-fdrtool



%description
This package implements the "shrinkage t" statistic introduced in
Opgen-Rhein and Strimmer (2007) and a shrinkage estimate of the
"correlation-adjusted t-score" (CAT score) described in Zuber and Strimmer
(2009).  It also offers a convenient interface to a number of other
regularized t-statistics commonly employed in high-dimensional
case-control studies.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.6-1
- initial package for Fedora
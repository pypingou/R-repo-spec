%global packname  dpa
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Dynamic Path Approach

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tcltk R-sem R-igraph 


BuildRequires:    R-devel tex(latex) R-tcltk R-sem R-igraph



%description
A GUI or command-line operated data analysis tool, for analyzing
time-dependent simulation data in which multiple instantaneous or
time-lagged relations are assumed. This package uses Structural Equation
Modeling (the sem package). It is aimed to deal with time-dependent data
and estimate whether a causal diagram fits data from an (agent-based)
simulation model.

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
%doc %{rlibdir}/dpa/html
%doc %{rlibdir}/dpa/DESCRIPTION
%{rlibdir}/dpa/INDEX
%{rlibdir}/dpa/help
%{rlibdir}/dpa/Meta
%{rlibdir}/dpa/R
%{rlibdir}/dpa/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora
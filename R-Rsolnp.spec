%global packname  Rsolnp
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.11
Release:          1%{?dist}
Summary:          General Non-linear Optimization

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-truncnorm 

BuildRequires:    R-devel tex(latex) R-stats R-truncnorm 

%description
General Non-linear Optimization Using Augmented Lagrange Multiplier Method

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
%doc %{rlibdir}/Rsolnp/DESCRIPTION
%doc %{rlibdir}/Rsolnp/CITATION
%doc %{rlibdir}/Rsolnp/doc
%doc %{rlibdir}/Rsolnp/html
%{rlibdir}/Rsolnp/Meta
%{rlibdir}/Rsolnp/data
%{rlibdir}/Rsolnp/NAMESPACE
%{rlibdir}/Rsolnp/R
%{rlibdir}/Rsolnp/INDEX
%{rlibdir}/Rsolnp/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.11-1
- initial package for Fedora
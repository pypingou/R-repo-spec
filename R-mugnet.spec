%global packname  mugnet
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.13.5
Release:          1%{?dist}
Summary:          Mixture of Gaussian Bayesian Network Model

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-catnet 

BuildRequires:    R-devel tex(latex) R-methods R-catnet 

%description
A package that models continuous multivariate data via directional acyclic
graphs and provides inference based on the frequentist approach

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.13.5-1
- initial package for Fedora
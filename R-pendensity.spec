%global packname  pendensity
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.3
Release:          1%{?dist}
Summary:          Density Estimation with a Penalized Mixture Approach

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-fda 

BuildRequires:    R-devel tex(latex) R-lattice R-fda 

%description
Estimating penalized (conditional) densities

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
%doc %{rlibdir}/pendensity/DESCRIPTION
%doc %{rlibdir}/pendensity/doc
%doc %{rlibdir}/pendensity/html
%{rlibdir}/pendensity/R
%{rlibdir}/pendensity/INDEX
%{rlibdir}/pendensity/NAMESPACE
%{rlibdir}/pendensity/help
%{rlibdir}/pendensity/Meta
%{rlibdir}/pendensity/data

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.3-1
- initial package for Fedora
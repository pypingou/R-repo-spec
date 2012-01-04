%global packname  gld
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.9.2
Release:          1%{?dist}
Summary:          Estimation and use of the generalised (Tukey) lambda distribution

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The generalised lambda distribution, or Tukey lambda distribution,
provides a wide variety of shapes with one functional form.  This package
provides random numbers, quantiles, probabilities, densities and plots
(for the density and distribution functions).  It also includes an
implementation of the starship estimation method for the distribution.

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
%doc %{rlibdir}/gld/html
%doc %{rlibdir}/gld/DESCRIPTION
%{rlibdir}/gld/help
%{rlibdir}/gld/R
%{rlibdir}/gld/INDEX
%{rlibdir}/gld/NAMESPACE
%{rlibdir}/gld/libs
RPM build errors:
%{rlibdir}/gld/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.9.2-1
- initial package for Fedora
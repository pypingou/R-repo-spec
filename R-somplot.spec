%global packname  somplot
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.05
Release:          1%{?dist}
Summary:          Visualisation of hexagonal Kohonen maps

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-hexbin 

BuildRequires:    R-devel tex(latex) R-hexbin 

%description
The package provides the plot function som.plot() to create high quality
visualisations of hexagonal Kohonen maps (self-organising maps).

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
%doc %{rlibdir}/somplot/DESCRIPTION
%doc %{rlibdir}/somplot/html
%{rlibdir}/somplot/INDEX
%{rlibdir}/somplot/test.data
%{rlibdir}/somplot/help
%{rlibdir}/somplot/Meta
%{rlibdir}/somplot/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.05-1
- initial package for Fedora
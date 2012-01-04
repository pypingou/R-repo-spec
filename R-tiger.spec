%global packname  tiger
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          TIme series of Grouped ERrors

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-e1071 R-hexbin R-qualV R-klaR R-som 

BuildRequires:    R-devel tex(latex) R-e1071 R-hexbin R-qualV R-klaR R-som 

%description
Temporally resolved groups of typical differences (errors) between two
time series are determined and visualized

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1-1
- initial package for Fedora
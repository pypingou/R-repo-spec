%global packname  oz
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.19
Release:          1%{?dist}
Summary:          Plot the Australian coastline and states

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-19.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Functions for plotting Australia's coastline and state boundaries.

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
%doc %{rlibdir}/oz/CITATION
%doc %{rlibdir}/oz/DESCRIPTION
%doc %{rlibdir}/oz/html
%{rlibdir}/oz/NAMESPACE
%{rlibdir}/oz/help
%{rlibdir}/oz/R
%{rlibdir}/oz/Meta
%{rlibdir}/oz/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.19-1
- initial package for Fedora
%global packname  CarbonEL
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Carbon Event Loop

Group:            Applications/Engineering 
License:          GPL version 2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-grDevices 

BuildRequires:    R-devel tex(latex) R-grDevices 

%description
This package hooks a Carbon event loop handler into R. This is useful for
enabling UI from a console R (such as using the Quartz device from
Terminal or ESS).

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora
%global packname  MarkedPointProcess
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.20
Release:          1%{?dist}
Summary:          Analysis of Marks of Marked Point Processes

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-RandomFields R-R2Cuba 

BuildRequires:    R-devel tex(latex) R-RandomFields R-R2Cuba 

%description
Non-parametric Analysis of the Marks of Marked Point Processes

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.20-1
- initial package for Fedora
%global packname  GriegSmith
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Uses Grieg-Smith method on 2 dimentional spatial data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-spatstat 

BuildRequires:    R-devel tex(latex) R-spatstat 

%description
The function GriegSmith accepts either quadrat count data, a point process
object(ppp) or a matrix of x and y coordinates. The function calculates a
nested analysis of variance and simulation envelopes.

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
%doc %{rlibdir}/GriegSmith/DESCRIPTION
%doc %{rlibdir}/GriegSmith/html
%{rlibdir}/GriegSmith/INDEX
%{rlibdir}/GriegSmith/NAMESPACE
%{rlibdir}/GriegSmith/help
%{rlibdir}/GriegSmith/R
%{rlibdir}/GriegSmith/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora
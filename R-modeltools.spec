%global packname  modeltools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.18
Release:          1%{?dist}
Summary:          Tools and Classes for Statistical Models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-18.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-stats4 

BuildRequires:    R-devel tex(latex) R-stats R-stats4 

%description
A collection of tools to deal with statistical models. The functionality
is experimental and the user interface is likely to change in the future.
The documentation is rather terse, but packages `coin' and `party' have
some working examples. However, if you find the implemented ideas
interesting we would be very interested in a discussion of this proposal.
Contributions are more than welcome!

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
%doc %{rlibdir}/modeltools/html
%doc %{rlibdir}/modeltools/DESCRIPTION
%{rlibdir}/modeltools/R
%{rlibdir}/modeltools/INDEX
%{rlibdir}/modeltools/help
%{rlibdir}/modeltools/NAMESPACE
%{rlibdir}/modeltools/LICENSE
%{rlibdir}/modeltools/Meta
%{rlibdir}/modeltools/CHANGES

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.18-1
- initial package for Fedora
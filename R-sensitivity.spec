%global packname  sensitivity
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Sensitivity Analysis

Group:            Applications/Engineering 
License:          CeCILL-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-boot 

BuildRequires:    R-devel tex(latex) R-boot 

%description
A collection of functions for factor screening and global sensitivity
analysis of model output.

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
%doc %{rlibdir}/sensitivity/DESCRIPTION
%doc %{rlibdir}/sensitivity/html
%{rlibdir}/sensitivity/help
%{rlibdir}/sensitivity/INDEX
%{rlibdir}/sensitivity/R
%{rlibdir}/sensitivity/Meta
%{rlibdir}/sensitivity/NAMESPACE
%{rlibdir}/sensitivity/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora
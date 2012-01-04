%global packname  pd.2006.07.18.mm8.refseq.promoter
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.99.0
Release:          1%{?dist}
Summary:          

Group:            Applications/Engineering 
License:          
URL:              https://r-forge.r-project.org/projects/%{packname}/index.html
Source0:          https://r-forge.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core




BuildRequires:    R-devel tex(latex) 



%description


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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.0-1
- initial package for Fedora
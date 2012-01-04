%global packname  PtProcess
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.3.0
Release:          1%{?dist}
Summary:          Time Dependent Point Process Modelling

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.3-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package fits and analyses time dependent marked point process models
with an emphasis on earthquake modelling. For a more detailed introduction
to the package, see the topic "PtProcess". A list of recent changes can be
found in the topic "Changes".

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
%doc %{rlibdir}/PtProcess/doc
%doc %{rlibdir}/PtProcess/DESCRIPTION
%doc %{rlibdir}/PtProcess/html
%doc %{rlibdir}/PtProcess/CITATION
%{rlibdir}/PtProcess/Meta
%{rlibdir}/PtProcess/INDEX
%{rlibdir}/PtProcess/NAMESPACE
%{rlibdir}/PtProcess/help
%{rlibdir}/PtProcess/data
%{rlibdir}/PtProcess/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.3.0-1
- initial package for Fedora
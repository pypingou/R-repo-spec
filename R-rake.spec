%global packname  rake
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Normalize sample weights using marginal total population weights.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Raking a survey dataset entails re-weighting a sample by making the sample
marginal totals agree with the population marginal totals for two survey
response variables. Raking is a robust technique that is often useful for
dealing with nonresponse. The 'rake' package streamlines the process of
Raking by creating the special 'rake' class, which is essentially a
summary of the sample weights.

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
%doc %{rlibdir}/rake/doc
%doc %{rlibdir}/rake/NEWS
%doc %{rlibdir}/rake/DESCRIPTION
%doc %{rlibdir}/rake/html
%{rlibdir}/rake/R
%{rlibdir}/rake/help
%{rlibdir}/rake/INDEX
%{rlibdir}/rake/NAMESPACE
%{rlibdir}/rake/data
%{rlibdir}/rake/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora
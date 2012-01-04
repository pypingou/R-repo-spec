%global packname  freqMAP
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Frequency Moving Average Plots (MAP) of Multinomial Data by a Continuous Covariate

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A frequency moving average plot (MAP) is estimated from a multinomial data
and a continuous covariate. The frequency MAP is a moving average estimate
of category frequencies, where frequency means and posterior bounds are
estimated. Comparisons of two frequency MAPs as well as odds ratios can be

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
%doc %{rlibdir}/freqMAP/DESCRIPTION
%doc %{rlibdir}/freqMAP/html
%{rlibdir}/freqMAP/NAMESPACE
%{rlibdir}/freqMAP/Meta
%{rlibdir}/freqMAP/INDEX
%{rlibdir}/freqMAP/R
%{rlibdir}/freqMAP/data
%{rlibdir}/freqMAP/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora
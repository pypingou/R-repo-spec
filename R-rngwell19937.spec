%global packname  rngwell19937
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.3
Release:          1%{?dist}
Summary:          WELL19937a random number generator implemented with 53 bit output

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A stand-alone package for the random number generator WELL19937a by F.
Panneton, P. L'Ecuyer and M. Matsumoto. The initialization algorithm
allows to seed the generator with a vector of integers of an arbitrary
length and uses MRG32k5a by P. L'Ecuyer to achieve good quality of the
initialization. The output function may be set to provide numbers from the
interval (0,1) with 53 (the default) or 32 random bits. WELL19937a is of
similar type as Mersenne Twister and has the same period. WELL19937a is
slightly slower than Mersenne Twister, but has better equidistribution and
"bit-mixing" properties and faster recovery from states with prevailing
zeros than Mersenne Twister. All WELL generators with orders 512, 1024,
19937 and 44497 can be found in randtoolbox package.

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
%doc %{rlibdir}/rngwell19937/html
%doc %{rlibdir}/rngwell19937/DESCRIPTION
%{rlibdir}/rngwell19937/LICENSE
%{rlibdir}/rngwell19937/INDEX
%{rlibdir}/rngwell19937/R
%{rlibdir}/rngwell19937/NAMESPACE
%{rlibdir}/rngwell19937/help
%{rlibdir}/rngwell19937/libs
%{rlibdir}/rngwell19937/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.3-1
- initial package for Fedora